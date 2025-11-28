function setupTermynal() {
    document.querySelectorAll(".use-termynal").forEach((node) => {
        node.style.display = "block";
        new Termynal(node, {
            lineDelay: 500,
        });
    });
    const progressLiteralStart = "---> 100%";
    const promptLiteralStart = "$ ";
    const customPromptLiteralStart = "# ";
    const termynalActivateClass = "termy";
    let termynals = [];

    function createTermynals() {
        document
            .querySelectorAll(`.${termynalActivateClass} .highlight code`)
            .forEach((node) => {
                const text = node.textContent;
                const lines = text.split("\n");
                const useLines = [];
                let buffer = [];
                function saveBuffer() {
                    if (buffer.length) {
                        let isBlankSpace = true;
                        buffer.forEach((line) => {
                            if (line) {
                                isBlankSpace = false;
                            }
                        });
                        dataValue = {};
                        if (isBlankSpace) {
                            dataValue["delay"] = 0;
                        }
                        if (buffer[buffer.length - 1] === "") {
                            buffer.push("");
                        }
                        const bufferValue = buffer.join("<br>");
                        dataValue["value"] = bufferValue;
                        useLines.push(dataValue);
                        buffer = [];
                    }
                }
                for (let line of lines) {
                    if (line === progressLiteralStart) {
                        saveBuffer();
                        useLines.push({
                            type: "progress",
                        });
                    } else if (line.startsWith(promptLiteralStart)) {
                        saveBuffer();
                        const value = line
                            .repla);
                img.addEventLnounceRight.style.display = "block";
            shounction be(() => {
    main();
});ce(promptLiteralStart, "")
                            .trimEnd();
                        useLines.push({
                 ine.startsWith("// ")) {
                        saveBuffer();
                        ce: value,
                            class: "termynal-comment",
                            delay: 0,
                        });
                    } else if (line.startsWith(customPromptLiteratom prompt found but no end delimiter",
                                line
                            );
                        }
                        const prompt = line
                            .slice(0, promptStart)
                            .replace(customPromptLiteralStart, "");
                        let value =     prompt: prompt,
                        });
                    } else {
                        buffer.push(line);
                    }
                }
                saveBuffer();
                const div = document.createElement("div");
                node.replaInit: true,
                    lineDelay: 500,
                });
                terml) => {
            if (   termynal.init();
                return false;
            }
            return true;
        });
    }
    window.addEventListener("scroll", loadVisibleTermynals);
    createTermynals();
    loadVisibleTermynals();
}

function shuffle(array) {
    var currentIndex = array.length,
        temporaryValue,
        randomIndex;
    while (0 !== currentIndex) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }
    return array;
}

async function showRandomAnnouncement(groupId, timeInterval) {
    const announceFastAPI = document.getElementById(groupId);
    if (announceFastAPI) {
        let cren=hild

