document.querySelectorAll(".copy-button").forEach(button => {

    button.addEventListener("click", () => {

        const code = button
            .closest(".codeblock")
            .querySelector("code")
            .innerText;

        navigator.clipboard.writeText(code);

        button.innerText = "Copied";

        setTimeout(() => {
            button.innerText = "Copy";
        },1500);

    });

});