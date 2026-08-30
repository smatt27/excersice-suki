#include "difference_of_squares.h"

namespace difference_of_squares {

// TODO: add your solution here
    int square_of_sum(int n){
        int sum_x = 0;
        for (int i = 1; i <= n;i++){
            sum_x += i;
        } 
        return sum_x * sum_x;
    }
    int sum_of_squares(int n){
        int sum_y = 0; 
        for (int i = 1; i<= n; i++){
            sum_y += i * i;
        }
        return sum_y;
    }
    int difference(int n){
         return square_of_sum(n) - sum_of_squares(n); 
    }
}  // namespace difference_of_squares
