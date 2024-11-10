console.log("Background generated")


chrome.contextMenus.create({
    id: "helloContextMenu",
    title: "Say jkjskjfs",
    contexts: ["selection"]
})


// Add an event listener for the context menu click
chrome.contextMenus.onClicked.addListener(function(info, tab) {
    if (info.menuItemId === 'helloContextMenu') {
        console.log("Menu item clicked with text:", info.selectionText);
        fetch('http://localhost:5000/highlight', {
            method: 'POST',
            headers: {
                'Content-type': 'application/json'
            },
            body: JSON.stringify({ word: info.selectionText })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            alert(data.message);
        })
        .catch(error => console.error('Error:', error));
    }
});