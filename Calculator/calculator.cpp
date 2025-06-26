#include <iostream>
#include <cmath>
#include <sstream>
#include <stack>
#include <cctype>
#include <stdexcept>
using namespace std;

class Calculator {
public:
    void run() {
        int choice;
        do {
            showMenu();
            cin >> choice;
            cin.ignore(); // flush newline

            switch (choice) {
                case 1: case 2: case 3: case 4: case 5:
                    performBasicOperation(choice);
                    break;
                case 6:
                    performModulus();
                    break;
                case 7:
                    evaluateExpression();
                    break;
                case 0:
                    cout << "Exiting calculator. Goodbye!" << endl;
                    break;
                default:
                    cout << "Invalid option. Try again." << endl;
            }

            cout << endl;

        } while (choice != 0);
    }

private:
    void showMenu() {
        cout << "======= Advanced Calculator =======" << endl;
        cout << "1. Addition (+)" << endl;
        cout << "2. Subtraction (-)" << endl;
        cout << "3. Multiplication (*)" << endl;
        cout << "4. Division (/)" << endl;
        cout << "5. Power (^)" << endl;
        cout << "6. Modulus (%)" << endl;
        cout << "7. Evaluate full expression (e.g., 3 + 5 * 2)" << endl;
        cout << "0. Exit" << endl;
        cout << "Select an option: ";
    }

    void performBasicOperation(int choice) {
        double a, b;
        cout << "Enter first number: ";
        cin >> a;
        cout << "Enter second number: ";
        cin >> b;

        switch (choice) {
            case 1:
                cout.precision(10);
                cout << "Result: " << (a + b) << endl;
                break;
            case 2:
                cout << "Result: " << (a - b) << endl;
                break;
            case 3:
                cout << "Result: " << (a * b) << endl;
                break;
            case 4:
                if (b == 0)
                    cout << "Error: Division by zero." << endl;
                else
                    cout << "Result: " << (a / b) << endl;
                break;
            case 5:
                cout << "Result: " << pow(a, b) << endl;
                break;
        }
    }

    void performModulus() {
        int x, y;
        cout << "Enter first integer: ";
        cin >> x;
        cout << "Enter second integer: ";
        cin >> y;

        if (y == 0) {
            cout << "Error: Modulus by zero." << endl;
        } else {
            cout << "Result: " << (x % y) << endl;
        }
    }

    // BONUS: Simple expression evaluator using stacks
    void evaluateExpression() {
        cin.ignore();
        string expr;
        cout << "Enter expression (e.g., 2 + 3 * (4 - 1)): ";
        getline(cin, expr);

        try {
            double result = evaluateInfix(expr);
            cout << "Result: " << result << endl;
        } catch (const exception& e) {
            cout << "Error: " << e.what() << endl;
        }
    }

    // Convert infix to postfix and evaluate it
    int precedence(char op) {
        if (op == '+' || op == '-') return 1;
        if (op == '*' || op == '/' || op == '%') return 2;
        if (op == '^') return 3;
        return 0;
    }

    double applyOp(double a, double b, char op) {
        switch (op) {
            case '+': return a + b;
            case '-': return a - b;
            case '*': return a * b;
            case '/':
                if (b == 0) throw runtime_error("Division by zero.");
                return a / b;
            case '%':
                return static_cast<int>(a) % static_cast<int>(b);
            case '^':
                return pow(a, b);
            default:
                throw runtime_error("Unknown operator.");
        }
    }

    double evaluateInfix(const string& tokens) {
        stack<double> values;
        stack<char> ops;

        for (size_t i = 0; i < tokens.length(); i++) {
            if (tokens[i] == ' ') continue;

            // Number parsing
            if (isdigit(tokens[i]) || tokens[i] == '.') {
                stringstream ss;
                while (i < tokens.length() &&
                       (isdigit(tokens[i]) || tokens[i] == '.')) {
                    ss << tokens[i++];
                }
                double val;
                ss >> val;
                values.push(val);
                i--; // reprocess the operator
            }
            else if (tokens[i] == '(') {
                ops.push(tokens[i]);
            }
            else if (tokens[i] == ')') {
                while (!ops.empty() && ops.top() != '(') {
                    double b = values.top(); values.pop();
                    double a = values.top(); values.pop();
                    char op = ops.top(); ops.pop();
                    values.push(applyOp(a, b, op));
                }
                ops.pop(); // remove '('
            }
            else { // Operator
                while (!ops.empty() && precedence(ops.top()) >= precedence(tokens[i])) {
                    double b = values.top(); values.pop();
                    double a = values.top(); values.pop();
                    char op = ops.top(); ops.pop();
                    values.push(applyOp(a, b, op));
                }
                ops.push(tokens[i]);
            }
        }

        while (!ops.empty()) {
            double b = values.top(); values.pop();
            double a = values.top(); values.pop();
            char op = ops.top(); ops.pop();
            values.push(applyOp(a, b, op));
        }

        return values.top();
    }
};
