import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, TextInput, Pressable } from 'react-native';
import React, { useState } from 'react';
import DateTimePicker from '@react-native-community/datetimepicker';
import Ionicons from 'react-native-vector-icons/Ionicons';
import RNPickerSelect from 'react-native-picker-select';


export default function App() {
    const tags = ['Active', 'Artsy', 'Beauty', 'Quick Snacks', 'Restaurants', 'Shopping', 'Nightlife'];
    const budgets = ['$-$$', '$$-$$$', '$$$-$$$$'];
    const [selectedTags, setSelectedTags] = useState([]);
    const [selectedBudget, setSelectedBudget] = useState([]);
    const [budget, setNewBudget] = useState([]);
    const [date, setDate] = useState(new Date());
    const [show, setShow] = useState(false);
    const [isPressed, setIsPressed] = useState(false);

  
    const onChange = (event, selectedDate) => {
      const currentDate = selectedDate;
      setShow(true);
      setDate(currentDate);
    };
    
    const setBudget = (value) => {
        if (value.length === 0) {
            setNewBudget([]);
            return;
        }
        else{
            const firstValue = value[0].split('-');
            const secondValue = value[value.length - 1].split('-');
        
            // Concatenate the first part of the first value with the second part of the second value
            const newValue = [firstValue[0], secondValue[1]];
            setNewBudget(newValue);
            console.log(newValue);
        }
    
        setSelectedBudget(value);
    }


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
        <View style={styles.tags}>
            {/* make each tag a button that can be selected */}
            {budgets.map(tag => (
                <Button
                    key={tag}
                    title={tag}
                    onPress={() => {
                        if (selectedBudget.includes(tag)) {
                            setBudget(selectedBudget.filter(t => t !== tag));
                        } else {
                            setBudget([...selectedBudget, tag]);
                        }
                    }}
                    // set the style to be pink if selected, otherwise purple
                    color={selectedBudget.includes(tag) ? 'pink' : 'gray'}
                />
            ))}
        </View>
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

    },
    budgetButtons: {
        flexDirection: 'row',
    }
});
