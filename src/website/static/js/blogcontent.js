

const classes = {
    "H1": "blogcontent-h1",
    "H2": "blogcontent-h2",
    "H3": "blogcontent-h3",
    "H4": "blogcontent-h4",
    "H5": "blogcontent-h5",
    "H6": "blogcontent-h6",
    "P": "blogcontent-p",
    "OL": "blogcontent-ol",
    "UL": "blogcontent-ul",
    "LI-OL": "blogcontent-ol-item",
    "LI-UL": "blogcontent-ul-item",
    "ITEM": "blogcontent-ol-item",
    "ITEM": "blogcontent-ul-item",
    "STRONG": "blogcontent-strong",
    "EM": "blogcontent-em",
    "IMG": "blogcontent-img",
    "A": "blogcontent-a",
    "HR": "blogcontent-hr",
    "BR": "blogcontent-br",
}


function addClass(object, parent) {
    var tagName = object.tagName
    if (parent == "OL") {
        tagName += "-OL"
    } else if (parent == "UL") {
        tagName += "-UL"
    }

    object.classList.add(classes[tagName])
    for (const child of object.children) {
        addClass(child, object.tagName)
    }
}

function addClassesToContent() {
    var contentContainer = document.getElementsByClassName("blogcontent-container")[0];
    for (const child of contentContainer.children) {
        addClass(child)
    }
}


function main() {
    addClassesToContent();
}


main();