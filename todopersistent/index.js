let items = ["hello world", "123"];

const itemsDiv = document.getElementById("items")



function renderItems() {
	itemsDiv.innerHTML = null;
	
	for (const [idx, item] of Object.entries(items)) {
		const container = document.createElement("div")
		container.style.marginBottom = "10px"
		
		const text = document.createElement("p")
		text.textContent = item;
		
		const button = document.createElement("button")
		buttton.textContent = "Delete"
		button.onclick = () => removeItem(idx)
		
		container.appendChild(text)
		container.appendChild(button)
		
		itemsDiv.appendchild(container)
		
		
		itemsDiv.appendChild(text)
	}
}
renderItems()

function loadItems() {}

function saveItems() {}

function addItem() {}

function remove Item() {}
