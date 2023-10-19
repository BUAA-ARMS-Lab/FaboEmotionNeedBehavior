/*
 * @Descripttion: 
 * @version: 
 * @Author: sueRimn
 * @Date: 2021-09-21 21:16:50
 * @LastEditors: Zhang Jiadong
 * @LastEditTime: 2023-04-25 15:42:15
 */
#include "perception_filter.h"

std::vector<social_msg::perception_msg>  perception_filter::per_list;


bool perception_filter::Whether_OK( social_msg::perception_msg per) {
        
        // 检测是否 重复;, 
        // 内容是完备
        if( per.intention == "" ||  per.p  == NULL  || per.IDtype ==""){
            return false;  /* intention为空的话,不传入prior need即可。 */
        }

        if( per.intention == "日常闲聊" || per.intention == "问询" || per.intention == "普通指令" ){
            return false;  
        }

        //用于当前测试
        if(per.person_name =="")
            per.person_name = "路人甲";

        //  时间  如果时间差小于阈值,则false； 如果大于阈值,说明很长时间没收到这类percepiton了,则true；
        for(auto iter = per_list.end(); iter != per_list.begin(); iter-- ){
            if(
                iter->person_name == per.person_name  
                &&  iter->IDtype == per.IDtype
                &&  iter->intention == per.intention  
                // &&  iter->speech_ == per.speech_   
              )
            {
                double diff = abs(iter->time - per.time);
                if( diff < time_thresh)  {
                    std::cout<<"意图过滤： "<<per.person_name<<"的"<<per.intention<<",相隔时间-----"<<diff<<"秒"<<std::endl;
                    return false; 
                }
            }
        }

        per_list.push_back( per );
        return true;
    }

