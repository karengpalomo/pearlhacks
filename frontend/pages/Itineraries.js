import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, ScrollView, Pressable, TextInput, Button } from 'react-native';
import React, { useState } from 'react';
import Modal from "react-native-modal";
import RNPickerSelect from 'react-native-picker-select';
import DateTimePicker from '@react-native-community/datetimepicker';
import axios from 'axios';

export default function Itineraries() {
    const [itineraries, setItineraries] = useState(['Itinerary 1', 'Itinerary 2', 'Itinerary 3']);
    const [itinerariesDescriptions, setItinerariesDescriptions] = useState(['Description 1', 'Description 2', 'Description 3']);
    const [itinerariesDates, setItinerariesDates] = useState(['Date 1', 'Date 2', 'Date 3']);
    const [itineraryGroups, setItineraryGroups] = useState(['Group 1', 'Group 2', 'Group 3']);
    const [itineraryIcon, setItineraryIcon] = useState(['🥾', '🌎', '🗼']);
    const [modalVisible, setModalVisible] = useState(false);
    const [itineraryVisible, setItineraryVisible] = useState(false);
    const [date, setDate] = useState(new Date());
    const [show, setShow] = useState(false);
    const [itineraryName, setItineraryName] = useState('');
    const [itineraryDescription, setItineraryDescription] = useState('');
    const [itineraryGroup, setItineraryGroup] = useState('');
    const [itineraryDate, setItineraryDate] = useState('');
    const [itinIcon, setItinIcon] = useState('');

    const onChange = (event, selectedDate) => {
        setItineraryDate(selectedDate);
        setDate(selectedDate);
        setShow(true);
        setItineraryDate(date.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' }));
        console.log(itineraryDate)
      };
  
    const submitItinerary = () => {
        // add the new itinerary to the list of itineraries
        console.log(itineraryDate)
        setItineraries([...itineraries, itineraryName]);
        setItinerariesDescriptions([...itinerariesDescriptions, itineraryDescription]);
        setItinerariesDates([...itinerariesDates, itineraryDate]);
        setItineraryGroups([...itineraryGroups, itineraryGroup]);
        setItineraryIcon([...itineraryIcon, itinIcon]);
        
        // close the modal
        setModalVisible(false);

        console.log(itinerariesDates)
    }

  return (
    
    <ScrollView style={styles.container}>
        {/* add button to add new itinerary */}
        <Pressable style={styles.addButton} 
            onPress={() => setModalVisible(true)}
        >
            <Text style={styles.buttonText}>+</Text>
        </Pressable>
        <Modal isVisible={modalVisible} >
            <View style={styles.form}>
                <Text style={styles.header2}>Add a new itinerary</Text>
                <TextInput
                    style={styles.formInput}
                    placeholder="Itinerary name"
                    onChangeText={(text) => setItineraryName(text)}
                />
                <TextInput
                    style={styles.formInput}
                    placeholder="Description"
                    onChangeText={(text) => setItineraryDescription(text)}
                />
                <RNPickerSelect
                    // style so that it is centered and pink
                    style={{
                        inputIOS: {
                            height: 40,
                            borderColor: 'pink',
                            borderWidth: 1,
                            padding: 10,
                            borderRadius: 10,
                            width: 200,
                            margin: 10,
                            marginLeft: 43,
                        },
                        inputAndroid: {
                            height: 40,
                            borderColor: 'pink',
                            borderWidth: 1,
                            padding: 10,
                            borderRadius: 10,
                            width: 200,
                            margin: 10,
                            marginLeft: 43,

                        },
                    }}
                    placeholder={{ label: 'Solo!', value: 'solo' }}
                    onValueChange={(value) => setItineraryGroup(value)}
                    // go through each group and create an item for it
                    items = {itineraryGroups.map((group) => {
                        return {label: group, value: group};
                    }
                    )}

                />
                <DateTimePicker
                    testID="dateTimePicker"
                    value={date}
                    mode={'date'}
                    onChange={onChange}
                    is24Hour={true}
                    accentColor='pink'
                />
                <RNPickerSelect
                    // style so that it is centered and pink
                    style={{
                        inputIOS: {
                            height: 40,
                            borderColor: 'pink',
                            borderWidth: 1,
                            padding: 10,
                            borderRadius: 10,
                            width: 200,
                            margin: 10,
                            marginLeft: 43,
                        },
                        inputAndroid: {
                            height: 40,
                            borderColor: 'pink',
                            borderWidth: 1,
                            padding: 10,
                            borderRadius: 10,
                            width: 200,
                            margin: 10,
                            marginLeft: 43,

                        },
                    }}
                    placeholder={{ label: 'Choose icon', value: '😃' }}
                    // go through each group and create an item for it
                    items={['🌎', '🗼', '🥾', '🚗', '🚲'].map((icon) => {
                        return {label: icon, value: icon};
                    }
                    )}
                    onValueChange={(value) => setItinIcon(value)}
                />
                <Pressable
                    style={styles.addItinerary}
                    onPress={() => submitItinerary()}
                >
                    <Text style={styles.buttonText}>Add</Text>
                </Pressable>
            </View>
        </Modal>
        {/* for each itinerary, create a view with all of its info */}
        {itineraries.map((itinerary, index) => {
            return (
                <Pressable
                    onPress={() => setItineraryVisible(true)}
                >
                <Modal isVisible={itineraryVisible} >
                    <View style={styles.form}>
                        <Text style={styles.header2}>{itinerary}</Text>
                        <Text>{itinerariesDescriptions[index]}</Text>
                        <Text>{itinerariesDates[index]}</Text>
                        <Text>{itineraryGroups[index]}</Text>
                    </View>
                    <Button title="Close" onPress={() => setItineraryVisible(false)} />
                </Modal>
                <View style={styles.itineraries} key={index}>
                    <View>
                        <Text style={styles.header1}>{itinerary}</Text>
                        <Text>{itinerariesDescriptions[index]}</Text>
                        <Text>{itinerariesDates[index]}</Text>
                        <Text>{itineraryGroups[index]}</Text>
                    </View>
                    <View style={styles.icon}>
                        <Text style={styles.iconText}>
                            {itineraryIcon[index]}
                        </Text>
                    </View>
                </View>
                </Pressable>
            );
        })}
      <StatusBar style="auto" />

    </ScrollView>
  );
}

const styles = StyleSheet.create({
    header1: {
        fontSize: 24,
        fontWeight: 'bold',
        marginBottom: 10,
    },
    header2: {
        fontSize: 20,
        fontWeight: 'bold',
        marginBottom: 10,
    },
  container: {
    flex: 1,
    backgroundColor: '#F5F7FB',
    paddingTop: 50,
  },

  addButton: {
      backgroundColor: 'pink',
      padding: 10,
      borderRadius: 10,
      margin: 10,
      height: 40,
      width: 40,
      shadowColor: 'gray',
      shadowOpacity: 0.5,
      shadowOffset: { width: 0, height: 2 },
        alignSelf: 'flex-end',
  },
    buttonText: {
        color: '#FFFF',
        fontSize: 16,
        textAlign: 'center',
    },
    icon: {
        borderRadius: 100,
        backgroundColor: '#F2C5BE',
        width: 60,
        height: 60,
        padding: 10,
    },
    iconText: {
        fontSize: 34,
        textAlign: 'center',
    },
    itineraries: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        backgroundColor: '#fff',
        padding: 20,
        borderRadius: 10,
        margin: 10,
    },
    form: {
        backgroundColor: '#fff',
        padding: 20,
        borderRadius: 10,
        margin: 10,
        alignItems: 'center',
    },
    addItinerary: {
        backgroundColor: 'pink',
        padding: 10,
        borderRadius: 10,
        margin: 10,
        height: 40,
        shadowColor: 'gray',
        shadowOpacity: 0.5,
        shadowOffset: { width: 0, height: 2 },
    },
    formInput: {
        height: 40,
        borderColor: 'pink',
        borderWidth: 1,
        padding: 10,
        borderRadius: 10,
        width: 200,
        margin: 10,
    }
});
