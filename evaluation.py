import sys
import numpy as np
import pandas as pd
from optparse import OptionParser

# Construct the list of predictors
PREDICTORS = [
    'yyyymmdd',
    'game_no',
    'weekday',
    'visiting_team',
    'visiting_team_league',
    'home_team',
    'home_team_league',
    'daytime',
    'park_id',
]

# Add the starting line-up for both teams:
# id, name, and defensive position
for prefix in ['home_', 'visiting_']:
    for j in range(1, 10):
        PREDICTORS.append(prefix+f'starting_player{j}_id')
        PREDICTORS.append(prefix+f'starting_player{j}_name')
        PREDICTORS.append(prefix+f'starting_player{j}_def_position')

def evaluate(alg, train_data, test_data, batchsize = 10):

    # Allow the algorithm to train itself
    alg.train(train_data)

    # Predictions container
    predicted = pd.Series(index = test_data.index)

    # Loop through test set and predict
    num_test = test_data.shape[0]
    j = 0
    while j < num_test:
        
        # Create batch
        batchlen = min(batchsize, num_test - j)
        batch = test_data.iloc[j:j+batchlen]
                    
        # Create identifying information
        batched_test_info = batch[PREDICTORS]

        # Predict
        predicted[batch.index] = alg.predict(batched_test_info)

        # Update
        alg.update(batch)

        # Increment j
        j += batchlen

    return predicted

# Helper functions to load the algorithms
def load_modules(alg_classes):
    """Each agent class must be in module class_name.lower().
    Returns a dictionary class_name->class"""

    def load(class_name):
        module_name = str(class_name).lower()  # by convention / fiat
        module = __import__(module_name)
        agent_class = module.__dict__[class_name]
        return (class_name, agent_class)

    return dict(map(load, alg_classes))


def main(args):

    # Fetch classnames
    usage_msg = 'python3 evaluation.py [algorithms]'
    parser = OptionParser(usage=usage_msg)
    (options, args) = parser.parse_args()

    if len(args) == 0:
        args = ['Baseline']

    # Load classes
    alg_classes = load_modules(args)
    alg_instances = {key:alg_classes[key]() for key in alg_classes}

    # Load training/test data
    nrows = 1000
    train_data = pd.read_csv('data/processed/train.csv', nrows=nrows)
    test_data = pd.read_csv('data/processed/test.csv', nrows=nrows)

    # Tiny bit of formatting for test set
    test_data = test_data.sort_values('yyyymmdd')

    # Evaluate
    all_predictions = pd.DataFrame(index=test_data.index, columns=args)
    for alg_name in alg_instances:
        all_predictions[alg_name] = evaluate(
            alg_instances[alg_name], train_data, test_data
        )
    print(all_predictions)


if __name__ == '__main__':

    main(sys.argv)


