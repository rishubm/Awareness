chrome.storage.sync.get(['isOn'], function(data) {
    const isOn = data.isOn || false;
    if(isOn) {
        analyze();
    }
});


function analyze() {
    const content = document.body.innerText;
    const keywords = extractKeyContent(content);
    scrapeLinks(keywords);
}

function extractKeyContent(content){
    const words = content.split(/\s+/);
    return words.slice(0, 5).join(' ')
}

function scrapeLinks(keywords){
    fetch('https://localhost:5000/scrape', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({url : 'https://www.google.com/search?q=${encodeURIComponent(keywords)}' })
    })
    .then(response => response.json)
    .then(data => {
        const links = data.links;
        display(links)
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function display(links) {
    const box = document.createElement('div');
    box.style.position = 'fixed';
    box.style.top = '20px';
    box.style.right = '20px';
    box.style.backgroundColor = '#fff';
    box.style.padding = '10px';
    box.style.border = '1px solid #ccc';
    box.style.zIndex = '9999';

    let htmlContent = '<strong> Relevant Links: </strong><br>';
    links.forEach(link => {
        htmlContent += '<a href = "${link}" target="_blank">${link}</a><br>';

    });


    box.innerHTML = htmlContent;
    document.body.appendChild(box);

}