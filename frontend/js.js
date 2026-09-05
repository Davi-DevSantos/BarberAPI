// ====== Aparence ======
// 

// ====== Integration ======
const API_BASE = window.location.origin;
const SCHEDULE_URL = `${API_BASE}/api/v1/schedule/registrar`;

function showToast(message, type = "info") {
    const container = document.querySelector(".toast-container");
    if (!container) return;
    const toast = document.createElement("div");
    toast.className = `toast ${type}`;
    toast.textContent = message;
    container.appendChild(toast);
    setTimeout(() => {
        toast.style.animation = "fadeOut 0.3s ease forwards";
        setTimeout(() => toast.remove(), 300);
    }, 4000);
}

function showMsg(elementId, text, isError = false) {
    const el = document.getElementById(elementId);
    if (!el) {
        showToast(text, isError ? "error" : "success");
        return;
    }
    el.textContent = text;
    el.className = `msg ${isError ? "error" : "success"} show`;
    clearTimeout(el._hideTimer);
    el._hideTimer = setTimeout(() => {
        el.classList.remove("show");
    }, 4000);
    showToast(text, isError ? "error" : "success");
}

async function handleResponse(response) {
    const data = await response.json().catch(() => ({}));
    if (!response.ok) {
        const detail = data.detail || JSON.stringify(data) || `Erro ${response.status}`;
        throw new Error(detail);
    }
    return data;
}

async function scheduleRequest() {
    const name = document.querySelector("#input-name").value().trim();
    const number = document.querySelector("#input-number").value();
    const email = document.querySelector("#input-email").value().trim();
    const service = document.querySelector("#input-service").value().trim();
    const date = document.querySelector("#input-date").value();

    if (!name || !number || !service || !date) {
        showMsg("msg-schedule", "preencha todos os campos necessario", true);
        return;
    }

    try {
        const response = await (SCHEDULE_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, number, email, service, date }),
        });
        const data = await handleResponse(response);
        console.log("Schedule OK", data);
        showMsg("msg-schedule", "agendamento concluido!");
    } catch (error) {
        console.log("Schedule Error:", error);
        showMsg("msg-schedule", error.message || "Falha no cadastro.", true);
    }
}

document.querySelector("#input-buttom")?.addEventListener("click", scheduleRequest)

window.schedulereq = scheduleRequest