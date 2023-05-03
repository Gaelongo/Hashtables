class Hashtable:
    
    def __init__(self, slots) -> None:
        self.table = []
        for i in range(0, slots):
            self.table.append(None)
    
    def __hash(self, key):
        
        h = 0
        
        for char in key:
            h += (h + ord(char) * 13)
            
        h = int(h % len(self.table))
            
        print(h)
        return h


    def set_item(self, key, valor):
        
        indice = self.__hash(key)
        
        if self.table[indice] == None:
            
            self.table[indice] = [[key, valor]]
            
        elif self.table[indice] != None:
            
            self.table[indice].append([key, valor])
        
        
    def get_item(self, key):
        
        indice = self.__hash(key)
        
        for i in range(0, len(self.table)):
            
            if self.table[indice][i][0] == key:
                return self.table[indice][i]
            
    
    def mostrar_tabla(self):
        
        print("IND  |   KEY  |   Valor")
        
        for i in range(0, len(self.table)):
            
            elemento = self.table[i]
            if elemento:
                for j in range(0, len(elemento)):
                    
                    print(f"{i}.  |   {elemento[j][0]}   |   {elemento[j][1]}")
            
            
            

def main():
    
    
    opc = 0
    
    tabla = None
    
    while opc != 5:
        
        print("""
              Menú:
              1. Crear tabla
              2. Agregar elemento
              3. Obtener elemento
              4. Mostrar tabla
              5. Salir""")
        opc = int(input("Ingrese una opción: "))
        
        match(opc):
            
            case 1:
                
                slots = int(input("Ingrese el número de casillas de la tabla: "))
                tabla = Hashtable(slots)
                print("Tabla creada correctamente.\n")
                
            case 2:
                
                key = input("Ingrese una key: ")
                valor = input("Ingrese el valor: ")
                tabla.set_item(key, valor)
                print("Se ha agregado correctamente el elemento.\n")
                
            case 3:
                
                key = input("Ingrese la key a buscar: ")
                elemento = tabla.get_item(key)
                print("Elemento encontrado: ")
                print(f"Key: {elemento[0]}, valor: {elemento[1]}")
                
            case 4:
                
                print("Mostrando tabla...")
                tabla.mostrar_tabla()

main() 