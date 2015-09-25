# Mozfest2015
Python/Django skeleton project for user driven ontology creation session at Mozfest2015

## Goal of the project
The goal of this project will be a user annotated ontology based on responses to images. The ontology will have 3 types of relationships: 
* is_a
* has_a
* does

Users will be shown a random selection of images and asked to answer 3 basic questions that correlate to these relationships. The responses are fed into a machine learning algorithm that will create nodes and links to form an ontology, which can be compared with the classification of these organisms by other means i.e. taxonomic.

## practical setup

A graciously donated Raspberry Pi by hosting the project via Apache will be setup on the event where users will be able to start annotating during explanation and demonstration. This will allow for live feedback on what the algorithm is doing and pitfalls that may occur in this live environment.
