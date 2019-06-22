const renderFile = data => {
    const file = document.createElement('div');
    file.classList.add('file');
    file.innerHTML = `
            <div class="header">
                <span>${data.filename}</span>
            </div>
            <pre><code class="${data.extension}">${data.text}</code></pre>
        `;
    return file;
};
const renderSnippet = data => {
    const snippet = document.createElement('div');
    snippet.classList.add('snippet');
    snippet.innerHTML = `
            <div class="header">
                <a href="/snippet/${data.snippet_id}">${data.title}</a>
            </div>
            ${data.frequency ? data.frequency.map(item => `
                <span>${item[0]}: ${item[1]} ${pronounceFile(item[1])}</span>
            `) : ""}
            <div class="files">
                ${data.files.map(file => renderFile(file).outerHTML).join("\n")}
            </div>
        `;
    return snippet;
};

const createEditor = () => {
    const textarea = document.createElement("div");
    textarea.classList.add('text-editor');
    textarea.innerHTML = `
        <input type="text" placeholder="filename" />
        <textarea class="code" />
        `;
    return textarea;
};
