#include "atbash_cipher.h"
#include <string> 
#include <cctype>

namespace atbash_cipher {

// TODO: add your solution here
    std::string encode(std::string text) {
        std::string Plain  = "abcdefghijklmnopqrstuvwxyz";
        std::string Cipher = "zyxwvutsrqponmlkjihgfedcba";
        std::string new_w = ""; 

    
        std::string cleaned = "";
        for (char i : text) {
            if (std::isalnum(i)) {
                cleaned += std::tolower(i);
            }
        }
        
        for (size_t i = 0; i < cleaned.length(); i++) {
            if (i > 0 && i % 5 == 0) {
                new_w += " ";
            }

            size_t posicion = Plain.find(cleaned[i]);
            if (posicion != std::string::npos) {
                new_w += Cipher[posicion];
            } else {
                new_w += cleaned[i]; 
            }
        }
        return new_w;
    }

    std::string decode(std::string text) {
        std::string Plain  = "abcdefghijklmnopqrstuvwxyz";
        std::string Cipher = "zyxwvutsrqponmlkjihgfedcba";
        std::string new_w = ""; 
        

        for (char i : text) {
            if (std::isalnum(i)) {
                size_t posicion = Cipher.find(i); 
                if (posicion != std::string::npos) {
                    new_w += Plain[posicion];   
                } else {
                    new_w += i;                  
                }
            }
        }
        return new_w;
    }

}  // namespace atbash_cipher
