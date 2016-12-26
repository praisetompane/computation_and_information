import React, { Component} from 'react';
import {AppRegistry, View} from 'react-native';

class FlexDimensionsBasics extends Component {
    render() {
        return(
            <View style={{flex: 1, flexDirection: 'column'}}>
                <View style={{flex: 1, backgroundColor: 'powderblue'}}/>
                <View style={{flex: 2, backgroundColor: 'skyblue'}}/>        
                <View style={{flex: 3, backgroundColor: 'red'}}/>                                 
            </View>
        );
    }
};

AppRegistry.registerComponent('df', () => FlexDimensionsBasics);