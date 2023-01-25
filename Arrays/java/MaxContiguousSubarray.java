public class MaxContiguousSubarray {
    

    static int maxContiguous(int[] array) {
        int maxSum = Integer.MIN_VALUE;
        int sum = 0;

        for (int i = 0; i < array.length; i++) {
            sum = sum + array[i];
            maxSum = Math.max(maxSum, sum);

            if (sum < 0) {
                sum = 0;
            }
        }

        return maxSum;
    }


    public static void main(String[] args) {
        int[] array = { 1, 2, 3, -2, 5 };
        int Result = maxContiguous(array);
        System.out.println(Result);
    }
}
