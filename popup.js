document.getElementById('encrypt_btn').addEventListener('click', () => {
    console.log("popup js encrypt_btn");
    // Send a message to the active tab to start the encryption process
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
        chrome.tabs.sendMessage(tabs[0].id, {action: 'encryptEmail'});
    });
});

// When button2 is clicked
document.getElementById('decrypt_btn').addEventListener('click', () => {
    console.log("popup js decrypt_btn");
    // Send a message to the active tab
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
        chrome.tabs.sendMessage(tabs[0].id, {action: 'decryptEmail'});
    });
});

