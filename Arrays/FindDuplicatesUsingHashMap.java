import java.util.*;
import java.util.Map.Entry;  


public class FindDuplicatesUsingHashMap {
    
    public static void main(String[] args) {

        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();//Creating HashMap  
        int[] inputArray = { 1, 2, 3, 4, 5, 6 ,6};
        for (int element : inputArray) {
            if (map.get(element) == null) {
                map.put(element, 1);
            } else {
                map.put(element, map.get(element) + 1);
            }
        }


    Set<Entry<Integer, Integer>> entrySet = map.entrySet();
         
    for (Entry<Integer, Integer> entry : entrySet) 
    {               
        if(entry.getValue() > 1)
        {
            System.out.println("Duplicate Element : "+entry.getKey()+" - found "+entry.getValue()+" times.");
        }
    }
    }
        
}
