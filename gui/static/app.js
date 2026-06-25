async function sendPost(url, data) {
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  if (!res.ok) throw new Error(`HTTP error: ${res.status}`);
  return await res.json();
}

document.querySelector("button").addEventListener("click", async () => {
    const result = await sendPost("/run-tool", {
        tool_name: "booker_stats",
        arguments: {}
    });
    document.querySelector("p").innerText = result.result;
});
