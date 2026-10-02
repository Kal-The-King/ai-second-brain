/**
 * Second Brain SDK - Embed anywhere
 * Usage: SecondBrain.init('user-id', 'api-url')
 */

window.SecondBrain = {
    userId: null,
    apiUrl: null,

    init(userId, apiUrl) {
        this.userId = userId;
        this.apiUrl = apiUrl;
    },

    async remember(text, category = 'general') {
        const response = await fetch(`${this.apiUrl}/remember`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text, category, user_id: this.userId })
        });
        return response.json();
    },

    async recall(query, limit = 5) {
        const response = await fetch(`${this.apiUrl}/recall`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query, limit, user_id: this.userId })
        });
        return response.json();
    },

    async searchWeb(query, limit = 5) {
        const response = await fetch(`${this.apiUrl}/search-web`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query, limit, user_id: this.userId })
        });
        return response.json();
    },

    async chat(message) {
        const response = await fetch(`${this.apiUrl}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: message, user_id: this.userId })
        });
        return response.json();
    },

    widget(selector) {
        const container = document.querySelector(selector);
        if (!container) return;

        container.innerHTML = `
            <div style="font-family: sans-serif; border: 1px solid #ddd; padding: 16px; border-radius: 8px;">
                <h3>Second Brain</h3>
                <input type="text" id="sb-input" placeholder="Ask me anything..." style="width: 100%; padding: 8px; margin-bottom: 8px; border: 1px solid #ddd; border-radius: 4px;">
                <div>
                    <button onclick="window.SecondBrain._remember()" style="background: #0066cc; color: white; padding: 8px 12px; border: none; border-radius: 4px; cursor: pointer; margin-right: 8px;">Remember</button>
                    <button onclick="window.SecondBrain._recall()" style="background: #0066cc; color: white; padding: 8px 12px; border: none; border-radius: 4px; cursor: pointer; margin-right: 8px;">Recall</button>
                    <button onclick="window.SecondBrain._searchWeb()" style="background: #0066cc; color: white; padding: 8px 12px; border: none; border-radius: 4px; cursor: pointer;">Search Web</button>
                </div>
                <div id="sb-results" style="margin-top: 16px; padding: 12px; background: #f5f5f5; border-radius: 4px; display: none;"></div>
            </div>
        `;
    },

    _remember() {
        const text = document.getElementById('sb-input').value;
        if (!text) return;
        this.remember(text).then(result => {
            document.getElementById('sb-results').innerHTML = 'Saved!';
            document.getElementById('sb-results').style.display = 'block';
        });
    },

    _recall() {
        const text = document.getElementById('sb-input').value;
        if (!text) return;
        this.recall(text).then(result => {
            const html = result.results.map(r => `<p><strong>${r.category}:</strong> ${r.text}</p>`).join('');
            document.getElementById('sb-results').innerHTML = html || 'No results';
            document.getElementById('sb-results').style.display = 'block';
        });
    },

    _searchWeb() {
        const text = document.getElementById('sb-input').value;
        if (!text) return;
        this.searchWeb(text).then(result => {
            const html = result.results.map(r => `<p><a href="${r.url}" target="_blank">${r.title}</a><br/>${r.snippet}</p>`).join('');
            document.getElementById('sb-results').innerHTML = html || 'No results';
            document.getElementById('sb-results').style.display = 'block';
        });
    }
};
