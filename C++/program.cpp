//Q1: Write an algorithm that simulates coin tossing. For each toss of the coin, the program should print Heads or Tails. Let the program toss the coin 100 times and count the number of times each side of the coin appears. Print the results. The program should call a separate function flip that takes no arguments and returns 0 for tails and 1 for heads.


#include <iostream>
#include <cstdlib>  // For rand() and srand()
#include <ctime>    // For time()

// Function to simulate a coin toss
int flip() {
    return rand() % 2; // Returns 0 for tails, 1 for heads
}

// Function to simulate coin tossing and count occurrences of Heads and Tails
void simulateCoinToss(int numTosses) {
    int headsCount = 0;
    int tailsCount = 0;

    for (int i = 0; i < numTosses; ++i) {
        int result = flip();
        if (result == 0) {
            tailsCount++;
            std::cout << "Tails\n";
        } else {
            headsCount++;
            std::cout << "Heads\n";
        }
    }

    // Print results
    std::cout << "\nResults:\n";
    std::cout << "Heads: " << headsCount << "\n";
    std::cout << "Tails: " << tailsCount << "\n";
}

int main() {
    // Seed the random number generator with the current time
    srand(static_cast<unsigned int>(time(nullptr)));

    // Simulate coin tossing 100 times
    simulateCoinToss(100);

    return 0;
}
