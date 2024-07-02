var lat, lon;

document.addEventListener("DOMContentLoaded", function () {
  setupIframe();

  var banner = document.getElementById("banner");
  var showListButton = document.getElementById("show_list");
  var isBannerOpen = true;

  showListButton.addEventListener("click", function () {
    if (isBannerOpen) {
      banner.classList.add("banner-hidden");
      showListButton.innerHTML = "&#x3e;"; // 오른쪽 화살표 아이콘 (열기)
      showListButton.setAttribute("aria-expanded", "false");
      document.getElementById("another").classList.add("full-cover");
    } else {
      banner.classList.remove("banner-hidden");
      showListButton.innerHTML = "&#x3c;"; // 왼쪽 화살표 아이콘 (닫기)
      showListButton.setAttribute("aria-expanded", "true");
      document.getElementById("another").classList.remove("full-cover");
    }
    isBannerOpen = !isBannerOpen;
  });
});

function setupIframe() {
  var iframe = document.querySelector("iframe");

  iframe.onload = function () {
    var iframeDocument = iframe.contentDocument;
    var popupElements = iframeDocument.querySelectorAll(".leaflet-marker-icon");
    var listElements = document.querySelectorAll(".li_store_list");

    listElements.forEach(function (listElement, index) {
      listElement.addEventListener("click", function (event) {
        var popupElement = popupElements[index];
        popupElement.click();
      });
    });

    let activeRequestController = null;

    popupElements.forEach(function (popupElement) {
      popupElement.addEventListener("click", function (event) {
        if (activeRequestController) {
          activeRequestController.abort();
        }

        activeRequestController = new AbortController();
        var signal = activeRequestController.signal;

        var waitForPopupLoaded = new Promise(function (resolve, reject) {
          var observer = new MutationObserver(function (
            mutationsList,
            observer
          ) {
            var popupPane = iframeDocument.querySelector(".leaflet-popup-pane");
            var popupContent = popupPane.querySelector(
              ".leaflet-zoom-animated"
            );

            if (popupContent && popupContent.children.length > 0) {
              observer.disconnect();
              resolve(popupContent);
            }
          });

          var popupPane = iframeDocument.querySelector(".leaflet-popup-pane");
          observer.observe(popupPane, { childList: true, subtree: true });
        });

        waitForPopupLoaded.then(function (popupContent) {
          var storeNameElement = popupContent.querySelector(".store_name");
          var storeName = storeNameElement.textContent;

          fetch("/store-info/" + storeName, { signal: signal })
            .then(function (response) {
              if (!response.ok) {
                throw new Error("Network response was not ok");
              }
              return response.json();
            })
            .then(function (data) {
              openPopup(popupContent, data, iframeDocument);
            })
            .catch(function (error) {
              if (error.name === "AbortError") {
                console.log("Fetch request was aborted");
              } else {
                console.error("Fetch Error:", error);
              }
            });
        });
      });
    });
  };
}

function openPopup(popupContent, data, iframeDocument) {
  var existingPopup = document.getElementById("popup");
  if (existingPopup) {
    existingPopup.remove();
  }

  var btnDetail = popupContent.querySelector(".btn_marker_detail");
  if (btnDetail) {
    btnDetail.onclick = function () {
      var storeName = data["Store_Name"];
      var popup = createPopup(data, iframeDocument);
      var space = document.querySelector("#another");
      space.appendChild(popup);

      popup.querySelector("#closePopup").onclick = function () {
        popup.remove();
      };

      popup.querySelector("#path").onclick = function () {
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function (position) {
            lat = position.coords.latitude;
            lon = position.coords.longitude;

            fetchNaverMap(data, lat, lon);
          }, handleGeolocationError);
        } else {
          console.log("Geolocation을 지원하지 않습니다.");
        }
      };
    };
  }
}

function createPopup(data, iframeDocument) {
  var popup = document.createElement("div");

  popup.style.position = "absolute";
  popup.id = "popup";
  popup.innerHTML = `
    <link rel="stylesheet" href="/static/pop.css">
    <header>
      <div id="titl">
        <h4 id="store_name">${data["Store_Name"]}</h4>
        <p id="store_hour">${data["hours"]}</p>
      </div>
      <img id="logo" src="/static/img/starbucks_logo.png" />
    </header>
    <main>
      ${createSection(data, "naver", "naver.png")}
      ${createSection(data, "google", "google.png")}
      ${createSection(data, "kakao", "kakaomap.png")}
    </main>
    <footer>
      <button id="closePopup">닫기</button>
      <button id="path">길안내</button>
    </footer>
  `;
  return popup;
}

function createSection(data, platform, logo) {
  var h3Text;
  if (platform === "google") {
    h3Text = `
      <h3 id="${platform}">
        <span class="${platform}-color-blue">G</span>
        <span class="${platform}-color-red">o</span>
        <span class="${platform}-color-yellow">o</span>
        <span class="${platform}-color-blue">g</span>
        <span class="${platform}-color-green">l</span>
        <span class="${platform}-color-red">e</span>
      </h3>`;
  } else if (platform === "kakao") {
    h3Text = `
      <h3 id="${platform}">
        <span id="${platform}_front">kakao</span>
        <span id="${platform}_back">map</span>
      </h3>`;
  } else {
    h3Text = `<h3 id="${platform}">${platform.toUpperCase()}</h3>`;
  }

  return `
    <div class="section">
      <div class="logo_section">
        <img id="${platform}_logo" class="logo" src="/static/img/${logo}" />
        ${h3Text}
      </div>
      <div class="info">
        <p class="info_title">평점: <span class="Rating">${
          data[`rating_${platform}`]
        }</span></p>
        <p class="info_title">평점 개수: <span class="RatingCount">${
          data[`rating_count_${platform}`]
        }</span></p>
        <p class="info_title">리뷰 개수: <span class="ReviewCount">${
          data[`review_count_${platform}`]
        }</span></p>
        <p class="info_title">리뷰 카테고리: <span class="ReviewCategory">${
          data[`review_keyword_${platform}`]
        }</span></p>
      </div>
    </div>
  `;
}

function fetchNaverMap(data, lat, lon) {
  var pathRequestController = new AbortController();
  var signal = pathRequestController.signal;
  storeName = data["Store_Name"];

  fetch("/naver-map/" + storeName, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-LAT": lat,
      "Y-LON": lon,
    },
    body: JSON.stringify(data),
    signal: signal,
  })
    .then(function (response) {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then(function (map_url) {
      var popupFeatures = {
        width: window.innerWidth * 0.6,
        height: window.innerHeight * 0.8,
        left: window.innerWidth * 0.5 - window.innerWidth * 0.3,
        top: window.innerHeight * 0.5 - window.innerHeight * 0.4,
        scrollbars: "yes",
        resizable: "yes",
        fullscreen: "yes",
      };

      var popupWindow = window.open(
        map_url,
        "_blank",
        stringifyPopupFeatures(popupFeatures)
      );
      popupWindow.moveTo(
        window.innerWidth * 0.5 - popupWindow.outerWidth * 0.5,
        window.innerHeight * 0.5 - popupWindow.outerHeight * 0.5
      );
    })
    .catch(function (error) {
      console.error("Fetch Error:", error);
    });
}

function handleGeolocationError(error) {
  var errorMessage = "";
  switch (error.code) {
    case error.PERMISSION_DENIED:
      errorMessage = "위치 정보를 허용해주세요.";
      break;
    case error.POSITION_UNAVAILABLE:
      errorMessage =
        "위치 정보를 사용할 수 없습니다. 브라우저 설정을 확인하거나 위치 서비스를 활성화하세요.";
      break;
    case error.TIMEOUT:
      errorMessage =
        "위치 정보를 가져오는 데 시간이 초과되었습니다. 다시 시도해주세요.";
      break;
    case error.UNKNOWN_ERROR:
      errorMessage = "알 수 없는 오류가 발생했습니다.";
      break;
    default:
      errorMessage = "알 수 없는 오류가 발생했습니다.";
  }
  console.error(errorMessage);
  alert(errorMessage);
}

function stringifyPopupFeatures(features) {
  return Object.keys(features)
    .map((key) => `${key}=${features[key]}`)
    .join(",");
}
