const highlight = selector => {
    document.querySelectorAll(selector).forEach(block => {
        hljs.highlightBlock(block)
    })
};
