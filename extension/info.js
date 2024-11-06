document.getElementById('Button').addEventListener('click', function() {
    chrome.storage.sync.get(['isOn'], function(data) {
        let isOn = data.isOn || false;
        isOn = !isOn;
        
        chrome.storage.sync.set({'isOn': isOn}, function() {
            document.getElementById('Button').textContent = isOn ? "Turn Off" : "Turn On";
        });

    });
});

chrome.storage.sync.get(['isOn'], function(data) {
    let isOn = data.isOn || false;
    document.getElementById('Button').textContent = isOn ? "Turn Off" : "Trun On";
});