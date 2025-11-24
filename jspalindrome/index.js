const quotes = [
  "The only way to do great work is to love what you do.",
  "In the middle of difficulty lies opportunity.",
  "Be yourself; everyone else is already taken.",
  "The best time to plant a tree was 20 years ago. The second best time is now.",
  "Success is not final, failure is not fatal: It is the courage to continue that counts.",
  "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.",
  "Life is what happens when you're busy making other plans.",
  "The future belongs to those who believe in the beauty of their dreams.",
  "It does not matter how slowly you go as long as you do not stop.",
  "Happiness is not something ready made. It comes from your own actions."
]

const usedIndexes = new Set()
const quoteElement = document.getElementById("quote")


function generateQuote() {
	if(usedIndexes.size >= quotes.length) {
		usedIndexes.clear()
	}

	while (true) {
		const randomIdx = Math.floor(Math.random() * quotes.length)
		
		if (usedIndexes.has(randomIdx)) continue
	
		const quote = quotes[randomIdx]
		quoteElement.innerHTML = quote;
		usedIndexes.add(randomIdx)
		break 
	}
}
