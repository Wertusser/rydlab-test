const renderFile = data => {
    const file = document.createElement('div');
    file.classList.add('file');
    file.innerHTML = `
            <div class="header">
                <span>${data.filename}</span>
            </div>
            <pre><code class="${data.extension}">${data.text.replace(/&/g,'&amp;')
        .replace(/</g,'&lt;')
        .replace(/>/g,'&gt;')}</code></pre>
        `;
    return file;
};
const renderSnippet = data => {
    const snippet = document.createElement('div');
    snippet.classList.add('snippet');
    snippet.innerHTML = `
            <div class="header">
                <a href="/snippet/${data.snippet_id}">${data.title || "untitled"}</a>
                <span>Created ${data.created_at}</span>
            </div>
            ${data.frequency ? data.frequency.map(item => `
                <span>${item[0]}: ${Math.floor((item[1] / data.amount) * 100)}%</span>
            `) : ""}
            <div class="files">
                ${data.files.map(file => renderFile(file).outerHTML).join("\n")}
            </div>
        `;
    return snippet;
};

const createEditor = (filename, text) => {
    const textarea = document.createElement("div");
    textarea.classList.add('text-editor');
    textarea.innerHTML = `
        <input class="filename" type="text" placeholder="filename" value="${filename}" />
        <textarea class="code">${text}</textarea>
        `;
    return textarea;
};
