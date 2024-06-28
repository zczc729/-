var lat, lon;

document.addEventListener("DOMContentLoaded", function () {
  setupIframe();
});

function setupIframe() {
  var iframe = document.querySelector("iframe");

  iframe.onload = function () {
    var iframeDocument = iframe.contentDocument;
    var popupElements = iframeDocument.querySelectorAll(
      ".leaflet-marker-icon.leaflet-zoom-animated.leaflet-interactive"
    );

    let activeRequestController = null;

    popupElements.forEach(function (popupElement) {
      popupElement.addEventListener("click", function (event) {
        if (activeRequestController) {
          activeRequestController.abort(); // 이전 요청 취소
        }

        activeRequestController = new AbortController();
        var signal = activeRequestController.signal;

        var iframe = document.querySelector("iframe");
        var iframeDocument = iframe.contentDocument;

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
              openPopup(popupContent, iframeDocument, data);
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

function openPopup(popupContent, iframeDocument, data) {
  // Close previous popup if exists
  var existingPopup = document.getElementById("popup");
  if (existingPopup) {
    existingPopup.remove();
  }

  // Create overlay

  var oldBtnDetail = popupContent.querySelector(".btn_marker_detail");
  if (oldBtnDetail) {
    oldBtnDetail.onclick = null;
  }

  var btnDetail = popupContent.querySelector(".btn_marker_detail");

  if (btnDetail) {
    btnDetail.onclick = function () {
      var storeName = data["매장명"];
      // var overlay = document.createElement("div");
      // overlay.id = "overlay";
      // document.body.appendChild(overlay);

      var popup = document.createElement("div");
      popup.style.position = "absolute";
      popup.id = "popup";

      popup.innerHTML = `
        <link rel="stylesheet" href="/static/pop.css">
        <header class="titl">
          <h4 id="store_name">${data["매장명"]}</h4>
          <p id="store_hour">${data["hours"]}</p>
          <img id="logo" src="/static/img/starbucks_logo.png" />
        </header>
        <main>
          <div class="section">
            <div class="logo_section">
              <img id="naver_logo" class="logo" src="/static/img/naver.png" />
              <h3 id="naver">NAVER</h3>
            </div>
            <div class="info">
              <p class="info_title">
                평점: <span id="naverRating">${data["별점"]}</span>
              </p>
              <p class="info_title">
                평점 개수: <span id="naverRatingCount">${data["별점 개수"]}</span>
              </p>
              <p class="info_title">
                리뷰 개수:
                <span id="naverReviewCount">${data["방문자 리뷰"]}</span>
              </p>
              <p class="info_title">
                리뷰 카테고리:
                <span id="naverReviewCategory">${data["리뷰 top 5"]}</span>
              </p>
            </div>
          </div>
          <div class="section">
            <div class="logo_section">
              <img id="google_logo" class="logo" src="/static/img/google.png" />
              <h3 id="google">
                <span class="google-color-blue">G</span>
                <span class="google-color-red">o</span>
                <span class="google-color-yellow">o</span>
                <span class="google-color-blue">g</span>
                <span class="google-color-green">l</span>
                <span class="google-color-red">e</span>
              </h3>
            </div>
            <div class="info">
              <p class="info_title">
                평점: <span id="googleRating">${data["구글평점"]}</span>
              </p>
              <p class="info_title">
                평점 개수:
                <span id="googleRatingCount">${data["구글평점수"]}</span>
              </p>
              <p class="info_title">
                리뷰 개수:
                <span id="googleReviewCount">${data["구글리뷰수"]}</span>
              </p>
              <p class="info_title">
                리뷰 카테고리:
                <span id="googleReviewCategory">${data["구글리뷰카테고리"]}</span>
              </p>
            </div>
          </div>
          <div id="last_section" class="section" style="padding-top: 10px">
            <div class="logo_section">
              <img id="kakao_logo" class="logo" src="/static/img/kakaomap.png" />
              <h3 id="kakao">
                <span id="kakao_front">kakao</span>
                <span id="kakao_back">map</span>
              </h3>
            </div>
            <div class="info">
              <p class="info_title">
                평점: <span id="kakaoRating">${data["kakao_rating"]}</span>
              </p>
              <p class="info_title">
                평점 개수:
                <span id="kakaoRatingCount">${data["kakao_rating_count"]}</span>
              </p>
              <p class="info_title">
                리뷰 개수:
                <span id="kakaoReviewCount">${data["kakao_review_count"]}</span>
              </p>
              <p class="info_title">
                리뷰 카테고리:
                <span id="kakaoReviewCategory"
                  >${data["카카오리뷰카테고리"]}</span
                >
              </p>
            </div>
          </div>
        </main>
        <footer>
          <button id="closePopup">닫기</button>
          <button id="path">길안내</button>
        </footer>
    `;

      iframeDocument.body.appendChild(popup);

      popup.querySelector("#closePopup").onclick = function () {
        popup.remove();
      };

      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
          lat = position.coords.latitude;
          lon = position.coords.longitude;
        });
      } else {
        console.log("Geolocation을 지원하지 않습니다.");
      }

      activeRequestController = new AbortController();
      signal = activeRequestController.signal;

      popup.querySelector("#path").onclick = function (storeName, signal) {
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function (position) {
            lat = position.coords.latitude;
            lon = position.coords.longitude;
          });
        } else {
          console.log("Geolocation을 지원하지 않습니다.");
        }

        var storeNameElement = popupContent.querySelector(".store_name");
        var storeName = storeNameElement.textContent;

        fetch("/naver-map/" + storeName, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-LAT": String(lat),
            "Y-LON": String(lon),
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
            var naverMapUrl = map_url;
            console.log(naverMapUrl);
            console.log(typeof naverMapUrl);
            var popupFeatures = {
              width: window.innerWidth * 0.6, // 화면 너비의 60%
              height: window.innerHeight * 0.8, // 화면 높이의 80%
              left: window.innerWidth * 0.5 - window.innerWidth * 0.3, // 화면 가운데 정렬을 위한 left 값
              top: window.innerHeight * 0.5 - window.innerHeight * 0.4, // 화면 가운데 정렬을 위한 top 값
              scrollbars: "yes", // 스크롤바 사용 여부
              resizable: "yes", // 크기 조절 가능 여부
              fullscreen: "yes", // 전체 화면 가능 여부
            };

            var popupWindow = window.open(
              naverMapUrl,
              "_blank",
              stringifyPopupFeatures(popupFeatures)
            );
            popupWindow.moveTo(
              window.innerWidth * 0.5 - popupWindow.outerWidth * 0.5,
              window.innerHeight * 0.5 - popupWindow.outerHeight * 0.5
            );
          })
          .catch(function (error) {
            if (error.name === "AbortError") {
              console.log("Fetch request was aborted");
            } else {
              console.error("Fetch Error:", error);
            }
          });
      };
    };
  } else {
    console.error("상세 정보 보기 버튼을 찾을 수 없음");
  }
}
function stringifyPopupFeatures(features) {
  return Object.keys(features)
    .map((key) => `${key}=${features[key]}`)
    .join(",");
}
