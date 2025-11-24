#include <iostream>
#include <vector>
using namespace std;

void print_menu(string name);
void print_list();
void add_item();
void delete_item();

vector<string> list;
string name;

int main(int arg_count, char *args[]) {
    if ( arg_count > 1 ) {
        name = string(args[1]);
        print_menu(name);
    }
    else {
        cout << "Username not supplied... exiting the program";
    }
    return 0;
}

void print_menu(string name) {
    int choice;

    cout << "*********************\n";
    cout << "1 - Print List.\n";
    cout << "2 - Add to list\n";
    cout << "3 - Delete from list.\n";
    cout << "4 - Quit.\n";
    cout << " Enter your choice and press return: ";

    cin >> choice;

    if( choice = 4 ){
        exit(0);
    }
    else {
        cout << "Sorry choice not implemented yet\n";
    }
}

void add_item() {
    cout << "\n\n\n\n\n\n\n";
    cout << "*** Add item ***\n";
    cout << "Type in an item and press enter: ";

    string item;
    cin >> item;

    list.push_back(item);

    cout << "Successfully added an item to the list \n\n\n\n\n";
    cin.clear();

    print_menu(name);
}
