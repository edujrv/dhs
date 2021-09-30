int buscar_max(int numeros[10]){
    int max = 0;
    for(int i = 0; i<10; i++){
        if( max < numeros[i]){
            max = numeros[i];
        }
    }
    return max;
}