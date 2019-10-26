//
// Created by Justin Wang on 10/19/2019.
//

#include "SubNode.hpp"

//SubNode::SubNode(std::string id, std::string course_name, bool required, bool taken) : MainNode::MainNode(id, course_name),
//                required(required), taken(taken) {}

bool SubNode::isRequired() const {
    return required;
}

bool SubNode::isTaken() const {
    return taken;
}
