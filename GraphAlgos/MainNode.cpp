//
// Created by Justin Wang on 10/18/2019.
//

#include "MainNode.hpp"
#include<string>

MainNode::MainNode (std::string id) : id(id) {}

const std::vector<MainNode*> &MainNode::getParents() const {
    return parents;
}

const std::vector<MainNode*> &MainNode::getChildren() const {
    return children;
}

const std::string &MainNode::getId() const {
    return id;
}

void MainNode::addParent(MainNode &node) {
    parents.push_back(&node);
}

void MainNode::addChild(MainNode &node) {
    children.push_back(&node);
}

//const std::string &MainNode::getCourseName() const {
//    return course_name;
//}
