public class sortArrayOfOs1sand2s {
// int [] arr={1,1,0,0,2,2,1,0}   ;
    static void sortArray(int[] array) {
        int l = 0;
        int m = 0;
        int h = array.length - 1;
        int i = 0;
        while (m < h) {
           
            if (array[m] == 1) {
                m++;
                continue;

            } else if (array[m] == 0) {
                int temp;
                temp = array[l];
                array[l] = array[m];
                array[m] = temp;
                l++;
                m++;

            } else if (array[m] == 2) {
                int temp;
                temp = array[m];
                array[m] = array[h];
                array[h] = temp;
                h--;

            }
            i++;
        }
    }

    static void printArray(int arr[]) {
     
        for (int i = 0; i < arr.length;i++){
         System.out.print(arr[i] );
         
        }
    System.out.println("");
  }

  public static void main(String[] args) {
     int [] arr={1,1,0,0,2,2,1,0}   ;
     sortArray(arr);
     printArray(arr);
        
    }
}
