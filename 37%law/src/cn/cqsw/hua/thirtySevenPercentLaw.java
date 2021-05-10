package cn.cqsw.hua;

import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.Random;
import java.util.Set;

import static java.lang.Math.random;

/**
 * @author laoxiehua
 * 37%定律，在已知队列中挑选以最大概率选择最好的
 * 规则：根据已知当前的长度size*37%,得到的值为一个界限值limits
 * 包括limits它前面的值，找到一个最大值max记录，从limits后开始
 * 如果找到比之前max还大的值就赋值并返回，如果没有找到就选择最后值返回
 */
public class thirtySevenPercentLaw {
    public static void main(String[] args) {
        int miss = 0;
        for (int i=0;i<100;i++){


        int size = 888999;
        int[] ints = randomArrays(size);
        int limits = (int) (size * 0.37);
//        System.out.println(limits);
//        print(ints);
        int max = 0;
        max = findMaxWithArray(0,limits,ints,max);
//        System.out.println();
//        System.out.println("max:"+max);
        int optimal = ints[ints.length-1];
        optimal = findMaxWithArray(limits,ints.length,ints,0);
//        System.out.println("optimal:"+optimal);
            if (optimal < max)
                miss++;

//        if (optimal < max){
//            miss++;
//            System.out.println("错过"+optimal+"最大值在前面为："+max);
//        }else if (optimal == max){
//            System.out.println("恭喜你找到了和前面一样的最优"+optimal);
//        }else if (optimal > max){
//            System.out.println("恭喜你在后面找到了最优"+optimal);
//        }

        }
        System.out.println("100次查找中错过"+miss+"次！");
    }

    public static int findMaxWithArray(int start,int end,int []arr,int max){
        for(int j=start;j<end;j++){
            if (arr[j]>max){
                max = arr[j];
            }
        }
        return max;
    }

    /**
     * 生成指定长度的随机数组
     * @param size
     * @return
     */
    public static int[] randomArrays(int size){
        int arr[] = new int[size];
        for(int i=0;i<arr.length;i++){
            arr[i] += (int) (Math.random()*1000000000+1);
        }
        return arr;
    }

    /**
     * 遍历数组
     * @param arr
     */
    public static void print(int[] arr){
        for (int a:arr){
            System.out.print(a+"\t");
        }
    }

}
