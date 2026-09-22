/* ==========================================================
   DOCS_OS Apple Code Block Engine v4
   Clipboard + Copy Button
========================================================== */

function copyCode(button){

    const block = button.closest(".codeblock");

    if(!block) return;

    const code = block.querySelector("pre code");

    if(!code) return;

    const text = code.innerText;

    navigator.clipboard.writeText(text).then(() => {

        const original = button.textContent;

        button.textContent = "Copied ✓";

        button.classList.add("copied");

        setTimeout(() => {
            button.textContent = original;
            button.classList.remove("copied");
        },1800);

    }).catch(() => {

        // Fallback for older browsers.
        const textarea = document.createElement("textarea");

        textarea.value = text;

        textarea.style.position = "fixed";
        textarea.style.opacity = "0";

        document.body.appendChild(textarea);

        textarea.select();
        document.execCommand("copy");

        document.body.removeChild(textarea);

        const original = button.textContent;

        button.textContent = "Copied ✓";

        button.classList.add("copied");

        setTimeout(() => {
            button.textContent = original;
            button.classList.remove("copied");
        },1800);

    });

}

/* Attach listeners after page loads */

document.addEventListener("DOMContentLoaded", () => {

    document.querySelectorAll(".copy-button").forEach((button) => {

        button.addEventListener("click", () => copyCode(button));

    });

});