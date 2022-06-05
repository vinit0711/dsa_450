public class MoveNegativeToOneSide {


    static void sortArray(int[] arr) {
        int l = 0;
        int r = arr.length - 1;

        while (l < r) {
            if (arr[l] < 0 && arr[r] > 0) {
                l++;
                r--;
                continue;
            } else if (arr[l] > 0 && arr[r] < 0) {
                int temp = arr[l];
                arr[l] = arr[r];
                arr[r] = temp;
                l++;
                r--;
            } else if (arr[l] > 0 && arr[r] > 0) {
                r--;
            } else {
                l++;
            }
        }
    }
   
        static void printArray(int arr[]) {
            
                for (int i = 0; i < arr.length;i++){
                System.out.print(arr[i] );
                
                }
            System.out.println("");
        }

    public static void main(String[] args) {
        int[] arr = { -1, -2, 2, -5, 6, -7, -9 };
        sortArray(arr);
        printArray(arr);

    }
}
