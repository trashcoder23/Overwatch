const API_BASE = ""  // works locally and in deployment


async function refreshMetrics() {

    try {

        const health = await fetch(`${API_BASE}/health`)
        const healthData = await health.json()

        document.getElementById("healthStatus").innerText = healthData.status

        const metrics = await fetch(`${API_BASE}/metrics`)
        const metricsData = await metrics.json()

        document.getElementById("latency").innerText = metricsData.latency_ms
        document.getElementById("errorRate").innerText = metricsData.error_rate.toFixed(3)

    } catch (err) {

        document.getElementById("healthStatus").innerText = "service unreachable"

    }

}



async function createUser() {

    const name = document.getElementById("usernameInput").value

    if (!name) return alert("Enter a name")

    await fetch(`${API_BASE}/api/users?name=${name}`, {
        method: "POST"
    })

    document.getElementById("usernameInput").value = ""

    loadUsers()
}



async function loadUsers() {

    const response = await fetch(`${API_BASE}/api/users`)
    const users = await response.json()

    const table = document.querySelector("#usersTable tbody")

    table.innerHTML = ""

    users.forEach(user => {

        const row = document.createElement("tr")

        row.innerHTML = `
            <td>${user.id}</td>
            <td>${user.name}</td>
            <td>${user.created_at}</td>
            <td>
                <button onclick="deleteUser(${user.id})">Delete</button>
            </td>
        `

        table.appendChild(row)

    })

}



async function deleteUser(id) {

    await fetch(`${API_BASE}/api/users/${id}`, {
        method: "DELETE"
    })

    loadUsers()
}



refreshMetrics()
