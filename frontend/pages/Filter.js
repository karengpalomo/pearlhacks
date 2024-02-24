import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, TextInput, Pressable } from 'react-native';
import React, { useState } from 'react';
import DateTimePicker from '@react-native-community/datetimepicker';
import Ionicons from 'react-native-vector-icons/Ionicons';
import RNPickerSelect from 'react-native-picker-select';
import Slider from '@react-native-community/slider';


export default function App() {
    const tags = ['tag1', 'tag2', 'tag3', 'tag4', 'tag5', 'tag6', 'tag7', 'tag8', 'tag9', 'tag10'];
    const [selectedTags, setSelectedTags] = useState([]);
    const [date, setDate] = useState(new Date());
    const [show, setShow] = useState(false);
    const [budget, setBudget] = useState(0);
  
    const onChange = (event, selectedDate) => {
      const currentDate = selectedDate;
      setShow(true);
      setDate(currentDate);
    };

    const formattedDate = date.toLocaleDateString('en-US', {
        month: 'long',
        day: 'numeric',
        year: 'numeric',
      });

    return (
    <View style={styles.container}>
      <View style={styles.section}>
        <Text style={styles.header2}>Select tags</Text>
        <View style={styles.tags}>
            {/* make each tag a button that can be selected */}
            {tags.map(tag => (
                <Button
                    key={tag}
                    title={tag}
                    onPress={() => {
                        if (selectedTags.includes(tag)) {
                            setSelectedTags(selectedTags.filter(t => t !== tag));
                        } else {
                            setSelectedTags([...selectedTags, tag]);
                        }
                    }}
                    // set the style to be pink if selected, otherwise purple
                    color={selectedTags.includes(tag) ? 'pink' : 'gray'}
                />
            ))}
        </View>
      </View>
      <View style={styles.datetime}>
        <View style={styles.section}>
            <Text style={styles.header2}>Date</Text>
            <DateTimePicker
                testID="dateTimePicker"
                value={date}
                mode={'date'}
                onChange={onChange}
                is24Hour={true}
                accentColor='pink'
            />
        </View>
        <View style={styles.section}>
            <Text style={styles.header2}>Time of day</Text>
            {/* radio list of morning, afternoon, or night where you can only select one time */}
            <RNPickerSelect
                style={{ inputIOS: { color: 'pink' }, inputAndroid: { color: 'pink' }, }}
                placeholder={{ label: 'Select a time of day', value: null }}
                onValueChange={(value) => console.log(value)}
                items={[
                    { label: 'Morning', value: 'morning' },
                    { label: 'Afternoon', value: 'afternoon'},
                    { label: 'Night', value: 'night' },
                ]}
            />
        </View>
      </View>
      <View style={styles.section}>
        <Text style={styles.header2}>Cost Range</Text>
        {/* slider to select a cost range */}
        <Slider
            style={{width: 300, height: 40}}
            minimumValue={0}
            maximumValue={100}
            minimumTrackTintColor="pink"
            maximumTrackTintColor="#000000"
            renderStepNumber={true}
            tapToSeek={true}
            StepMarker = {true}
            step={5}
            onSlidingComplete={(value) => setBudget(value)}
        />
        <Text>
            $0 - ${budget}
        </Text>
      </View>
        <View style={styles.section}>
            <Text style={styles.header2}>Number of People</Text>
            <TextInput
                style={{ height: 40, borderColor: 'pink', borderWidth: 1, padding: 10, borderRadius: 10}}
                keyboardType='numeric'
                placeholder='Enter a number'
            />
        </View>
        {/* make a submit button for date, budget, time of day, and tags selected */}
        <Pressable
            style={{backgroundColor: 'pink', padding: 10, borderRadius: 10, margin: 10, height: 40, shadowColor: 'gray',shadowOpacity: 0.5, shadowOffset: { width: 0, height: 2 },
            }}
            onPress={() => console.log('submit')}
        >
            <Text style={styles.btnText}>Submit</Text>
        </Pressable>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
    header2: {
        fontSize: 20,
        fontWeight: 'bold',
        marginBottom: 10,
    },

  container: {
    flex: 1,
    backgroundColor: '#F5F7FB',
  },
  section: {
    backgroundColor: '#fff',
    justifyContent: 'center',
    margin: 10,
    padding: 20,
    borderRadius: 10,
  },
    tags: {
        flexDirection: 'row',
        flexWrap: 'wrap',
        alignItems: 'center',
        justifyContent: 'center',
    },
    datetime: {
        flexDirection: 'row',
    },
    btnText: {
        color: '#FFFF',
        fontSize: 16,
        textAlign: 'center',

    }
});
