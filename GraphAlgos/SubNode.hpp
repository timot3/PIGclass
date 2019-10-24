//
// Created by Justin Wang on 10/19/2019.
//

#ifndef PIGCLASS_SUBNODE_HPP
#define PIGCLASS_SUBNODE_HPP

#include<string>

#include "MainNode.hpp"
//#include "DisjointSet.cpp"


class SubNode : MainNode {
private:
    bool required;
    bool taken;
//    DisjointSet DSet;
public:
    SubNode(std::string id, std::string course_name, bool required, bool taken);

    bool isRequired() const;

    bool isTaken() const;
};


#endif //PIGCLASS_SUBNODE_HPP
