/* ==========================================================
   DOCS_OS Premium Code Blocks v3
   Copy Button Engine
========================================================== */

(function () {

    function initCodeBlocks() {

        const blocks = document.querySelectorAll(".codeblock");

        blocks.forEach((block) => {

            const button = block.querySelector(".copy-button");
            const code = block.querySelector("pre code");

            if (!button || !code) return;

            button.addEventListener("click", async () => {

                const text = code.textContent;

                try {

                    await navigator.clipboard.writeText(text);

                    button.classList.add("copied");
                    button.textContent = "Copied ✓";

                    setTimeout(() => {
                        button.classList.remove("copied");
                        button.textContent = "Copy";
                    }, 1800);

                } catch (err) {

                    // Fallback for older browsers
                    const textarea = document.createElement("textarea");

                    textarea.value = text;
                    textarea.style.position = "fixed";
                    textarea.style.opacity = "0";

                    document.body.appendChild(textarea);

                    textarea.focus();
                    textarea.select();

                    document.execCommand("copy");

                    document.body.removeChild(textarea);

                    button.classList.add("copied");
                    button.textContent = "Copied ✓";

                    setTimeout(() => {
                        button.classList.remove("copied");
                        button.textContent = "Copy";
                    }, 1800);

                }

            });

        });

    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initCodeBlocks);
    } else {
        initCodeBlocks();
    }

})();