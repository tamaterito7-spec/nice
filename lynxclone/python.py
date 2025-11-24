#!/usr/bin/env python3
"""
tinybrow - a 3-file, 80-line text browser
Features: GET/HTTPS, <h1>-<h6>, <p>, <a>, <ul>/<li>, <pre>, link menu
"""
import urllib.request, urllib.parse, sys
from html.parser import HTMLParser

class Browser(HTMLParser):
	def __init__(self):
		super().__init__()
		self.links = []
		self.out = []
		self.in_pre = False
	
	def handle_starttag(self, tag, attrs):
		attrs = dict(attrs)
		if tag == 'a' and 'href' in attrs:
			text = attrs.get('title', '[link]')
			self.links.append((text, attrs['href']))
			self.out.append(f"[{len(self.links)}] {text}")
		elif tag == 'pre':
			self.in_pre = True
	
	def handle_endtag(self, tag):
		if tag == 'pre': self.in_pre = False
		
	def handle_data(self, data):
		data = data.strip()
		if not data: return
		if self.in_pre:
			self.out.append(data)
		else:
			if self.lasttag in {f'h{i}' for i in range(1,7)}:
				self.out.append("\n" + data.upper())
			elif self.lasttag in {'p', 'li'}:
				self.out.append(data)
				
def fetch(url):
	if not url.startswith(('http://', 'https://')):
		url = 'https://' + url
	req = urllib.request.Request(url, headers={'User-Agent': 'tinybrow/0.1'})
	with urllib.request.urlopen(req, timeout=10) as r:
		html = r.read().decode('utf-8', errors='replace')
	return html, r.geturl()
	
def render(page):
	p = Browser()
	p.feed(page)
	print("\n".join(p.out))
	print("\n--- LINKS ---")
	for i, (text, url) in enumerate(p.links, 1):
		print(f"[{i}] {text} → {url}")
	return p.links
	
def main(start_url):
	url = start_url
	while True:
		try:
			print(f"\nFetching {url}")
			html, url = fetch(url)
			links = render(html)
			if not links:
				print("\nNo links found. Enter new URL or q to quit.")
				choice = input("\n> ").strip()
				if choice == 'q': break
				if choice.isdigit() and 1 <= int(choice) <= len(links):
					url = urllib.parse.urljoin(url, links[int(choice)-1][1])
				elif choice:
					url = choice
		except KeyboardInterrupt:
			print("\nBye!")
			break
		except Exception as e:
			print(f"Error: {e}")
			choice = input("New URL or q: ")
			if choice == 'q': break
			url = choice
					
if __name__ == '__main__':
	url = sys.argv[1] if len(sys.argv)>1 else "https://example.com"
	main(url)
