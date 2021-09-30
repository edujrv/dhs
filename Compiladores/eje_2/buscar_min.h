int buscar_min(int numeros[10]){
    int min = 99999999;
    for(int i = 0; i<10; i++){
        if(min > numeros[i]){
            min = numeros[i];
        }
    }
    return min;
}