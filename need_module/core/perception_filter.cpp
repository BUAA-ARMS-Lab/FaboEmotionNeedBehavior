/*
 * @Descripttion: 
 * @version: 
 * @Author: sueRimn
 * @Date: 2021-09-21 21:16:50
 * @LastEditors: Zhang Jiadong
 * @LastEditTime: 2023-04-25 15:42:15
 */
#include "perception_filter.h"

std::vector<social_msg::perception_msg>  perception_filter::per_filter_list;


bool perception_filter::Whether_OK( social_msg::perception_msg& per) {
        
        // 检测是否 重复;, 
        // 内容是完备
        if( per.intention == "" ||  per.p  == NULL  || per.IDtype ==""){
            return false;  /* intention为空的话,不传入prior need即可。 */
        }

        // 家庭和医院场景下基本都是对话，所以直接回复true
        if(per.scene=="family"  ||  per.scene=="hospital")
            return true;
            
        // 过滤掉无用的意图。 TODO: 由课题二重新训练神经网络
        if( /* per.intention == "日常闲聊" || */ per.intention == "家长验证" || per.intention == "普通指令" ){
            return false;  
        }

        //用于10月的测试
        // if(per.person_name =="")
            // per.person_name = "路人甲";


        //  时间  如果时间差小于阈值,则false； 如果大于阈值,说明很长时间没收到这类percepiton了,则true；
        std::cout<<"         【意图过滤】 "<<per.scene<<"下"<<per.person_name<<"的"<<per.intention<<std::endl;
        for(int i=per_filter_list.size()-1; i>=0; i--){
            social_msg::perception_msg temp = per_filter_list[i];
            std::cout   <<"         【现存意图】 ：IDtype:"<<temp.IDtype
                        <<", person_name:"<<temp.person_name
                        <<", scene:"<<temp.scene
                        <<", intention:"<<temp.intention            <<std::endl;

            if(
                temp.person_name == per.person_name  
                &&  temp.IDtype == per.IDtype
                &&  temp.intention == per.intention  
                &&  temp.speech == per.speech   
              )
            {
                double diff = abs(temp.time - per.time);
                if( diff < time_thresh)  {
                    std::cout<<"         【相隔时间】 -----  "<<diff<<"秒"<<std::endl;
                    // printf(  WHITE "         【意图过滤】 %c的%c相隔时间%f秒"NONE, per.person_name,per.intention,diff);
                    return false; 
                }
            }
        }
        

        per_filter_list.push_back( per );
        return true;
    }

