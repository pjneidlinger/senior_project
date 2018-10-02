all:
	g++ BasketballApp.cpp -o BasketballApp
	./BasketballApp

clean:
	rm data.txt
	rm BasketballApp
