function activePageCheck() {
    // Checks for the active page and update the navbar
    const pageName = document.getElementById("pageName").textContent;
    document.getElementById(pageName).classList.add("active");
}

function getImage() {
    // Microservice Function by Steven Au
    // Get the image of the day
    const url = "https://programming-languages-compare.herokuapp.com/api";
    fetch(url)
        .then(object => object.json())
        .then(function(item) {
            let originalImage = document.getElementById("imageOfTheDay");

            // Javascript recursion
            if (item["full"] === originalImage.src) {
                // Recursive call to ensure a different image
                getImage();
            }
            originalImage.src = item["full"];
        }
    );
 }

function redirectHome() {
    // Redirect user back to origin after 7 seconds. (Used in 404 page)
    setTimeout(function() {
        window.location.href = '/';
    }, 7000);
}

function pauseUpdateButton() {
    // Pause the update image/time button for a few seconds
    document.getElementById("updateButton").disabled = true;
    setTimeout(function() {
        document.getElementById("updateButton").disabled = false;
    }, 3000);
}

function reloadHome() {
    // Citation for the following:
    // Date: 2/10/2022
    // Source: https://developer.mozilla.org/en-US/docs/Web/API/PerformanceNavigationTiming/type
    // Detect if the load was a back button.
    let reloadType = performance.getEntriesByType("navigation")[0].type

    // Bypass a bug without clearing the user cache where the timer was not implemented
    if (reloadType === "back_forward"){
        window.location.reload()
    }
}

function getTime() {
    // Microservice by Andrew Layendecker - fetching his data.
    // Get the Pacific time
    const url = "https://time-microservice-04.herokuapp.com/api/time";
    fetch(url)
        .then(object => object.json())
        .then(item =>
	        document.getElementById("time").textContent=item[1]["standardTime"]
    );
}

function checkSubmission() {
    // Verify if a submission was recently made.
    reloadHome()
    if (document.getElementById("dateLastSubmitted")) {
        const originalTime = parseInt(document.getElementById("dateLastSubmitted").innerText);
        const url = "https://time-microservice-04.herokuapp.com/api/time"; // Time microservice
    
        // Set up
        const remainderTime = document.getElementById("timeRemainder");
        const submitMessage = document.getElementById("submitMessage");
        const submitButton = document.getElementById("formSubmit");
        const maxTimer = 20000; // 20 seconds
    
        fetch(url)
            .then(object => object.json())
            .then(function(item) {
    
                const currentTime = item[1]["unixNumberGMT"];
                const timeDif = Math.abs(currentTime - originalTime);
    
                // 20 seconds delay since the previous request.
                if (timeDif < maxTimer) {
                    submitMessage.hidden = false;
                    submitButton.disabled = true;

                    // Remainder is the difference rounded up - note that time is calculated by 1000, so change to
                    // a whole integer.
                    let remainder = Math.ceil((maxTimer - timeDif)/1000);

                    // Get the interval and interval id for later stopping
                    let interId = setInterval(function() {
                        remainder -= 1;
                        remainderTime.textContent = remainder - 1;
                    }, 1000)
    
                    // Stop the infinite timer
                    if (remainder === 0) {
                        clearInterval(interId);
                    }

                    // Time out to the end.
                    setTimeout(function() {
                        submitButton.disabled = false;
                        submitMessage.hidden = true;
                    }, maxTimer - timeDif)
                }
            }
        );
    }
}

function syntaxEqualizer() {
    // Make both size of the syntax panel the same based on the largest size
    let leftSize = document.getElementById("left-data").offsetHeight
    let rightSize = document.getElementById("right-data").offsetHeight

    if (leftSize > rightSize) {
        document.getElementById("right-data").style.height = leftSize + "px"
        document.getElementById("left-data").style.height = leftSize + "px"
    } else {
        document.getElementById("right-data").style.height = rightSize + "px"
        document.getElementById("left-data").style.height = rightSize + "px"
    }
}