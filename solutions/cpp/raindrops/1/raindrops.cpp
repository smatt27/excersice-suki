#include "raindrops.h"

namespace raindrops {
    
    // TODO: add your solution here
    std::string convert(int numero){
        std::string resul = "";

        if(numero % 3 == 0) resul += "Pling";
        if(numero % 5 == 0) resul += "Plang";
        if(numero % 7 == 0) resul += "Plong"; 

        if (resul.empty()) {
            return std::to_string(numero);
        }
        return resul; 
    }

}  // namespace raindrops
