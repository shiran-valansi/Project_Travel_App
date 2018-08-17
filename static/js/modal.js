
    console.log("in modal.js");
    var modal = document.querySelector(".modal");
    // var addButton = document.querySelector(".addButton");
    var closeButton = document.querySelector(".close-button");

    function toggleModal() {
        console.log("in toggle modal function");
        modal.classList.toggle("show-modal");
    }

    function windowOnClick(event) {
        if (event.target === modal) {
            toggleModal();
        }
    }

    // addButton.addEventListener("click", toggleModal);
    closeButton.addEventListener("click", toggleModal);
    window.addEventListener("click", windowOnClick);
    