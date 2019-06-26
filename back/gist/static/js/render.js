const renderFile = data => {
    const file = document.createElement('div');
    file.classList.add('file');
    file.innerHTML = `
            <div class="header">
                <span>${data.filename}</span>
            </div>
            <pre><code class="${data.extension}">${data.text.replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')}</code></pre>
        `;
    return file;
};
const renderSnippet = (data) => {
    const snippet = document.createElement('div');
    snippet.classList.add('snippet');
    snippet.innerHTML = `
            <div class="header">
                <a href="/snippet/${data.snippet_id}">${data.title || "untitled"}</a>
                <span>Created ${data.created_at}</span>
            </div>
            ${data.statistic ? data.statistic.map(item => `
                <span>${item[0]}: ${item[1]} ${pronounceFile(item[1])}</span>
            `) : ""}
            <div class="files">
                ${data.isFull ?
        data.files.map(file => renderFile(file).outerHTML).join("\n") :
        renderFile(data.file).outerHTML}
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

const createStatistic = (data) => {
    const statistic = document.createElement("div");
    statistic.classList.add('statistic');
    statistic.innerHTML = data.result.langs.map(item => `
    <span>${item.name}: ${item.amount}%</span>
    `).join(", ");
    return statistic;
};
