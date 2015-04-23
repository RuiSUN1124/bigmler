# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2015 BigML
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


""" Testing analyze subcommand

"""
from world import world, setup_module, teardown_module, teardown_class

import basic_tst_prediction_steps as test_pred
import dataset_advanced_steps as dataset
import evaluation_steps as evaluation


class TestAnalyze(object):

    def teardown(self):
        """Calling generic teardown for every method

        """
        teardown_class()

    def setup(self):
        """No setup operations for every method at present

        """
        pass

    def test_scenario1(self):
        """
            Scenario: Successfully building k-fold cross-validation from dataset:
                Given I create BigML dataset uploading train "<data>" file in "<output>"
                And I check that the source has been created
                And I check that the dataset has been created
                And I create BigML <kfold>-fold cross-validation
                And I check that the <kfold>-datasets have been created
                And I check that the <kfold>-models have been created
                And I check that the <kfold>-fold cross-validation has been created
                Then the evaluation file is like "<json_evaluation_file>"

                Examples:
                | data             | output                    | kfold | json_evaluation_file               |
                | ../data/iris.csv | ./scenario_a_1/evaluation | 2     | ./check_files/evaluation_kfold.json |
        """
        print self.test_scenario1.__doc__
        examples = [
            ['data/iris.csv', 'scenario_a_1/evaluation', '2', 'check_files/evaluation_kfold.json']]
        for example in examples:
            print "\nTesting with:\n", example
            test_pred.i_create_dataset(self, data=example[0], output=example[1])
            test_pred.i_check_create_source(self)
            test_pred.i_check_create_dataset(self)
            test_pred.i_create_kfold_cross_validation(self, k_folds=example[2])
            test_pred.i_check_create_kfold_datasets(self, example[2])
            test_pred.i_check_create_kfold_models(self, example[2])
            test_pred.i_check_create_kfold_cross_validation(self, example[2])
            evaluation.then_the_evaluation_file_is_like(self, example[3])

    def test_scenario2(self):
        """
            Scenario: Successfully building feature selection from dataset:
                Given I create BigML dataset uploading train "<data>" file in "<output>"
                And I check that the source has been created
                And I check that the dataset has been created
                And I create BigML feature selection <kfold>-fold cross-validations improving "<metric>"
                And I check that the <kfold>-datasets have been created
                And I check that the <kfold>-models have been created
                And I check that all the <kfold>-fold cross-validations have been created
                Then the best feature selection is "<selection>", with "<metric>" of <metric_value>

                Examples:
                | data                | output                    | kfold | metric   | selection   | metric_value
                | ../data/iris_2f.csv | ./scenario_a_2/evaluation | 2     | accuracy | petal width | 100.00%
                | ../data/iris_2f.csv | ./scenario_a_3/evaluation | 2     | phi      | petal width | 1
        """
        print self.test_scenario2.__doc__
        examples = [
            ['data/iris_2f.csv', 'scenario_a_2/evaluation', '2', 'accuracy', 'petal width', '100.00%'],
            ['data/iris_2f.csv', 'scenario_a_3/evaluation', '2', 'phi', 'petal width', '1']]
        for example in examples:
            print "\nTesting with:\n", example
            test_pred.i_create_dataset(self, data=example[0], output=example[1])
            test_pred.i_check_create_source(self)
            test_pred.i_check_create_dataset(self)
            test_pred.i_create_kfold_cross_validation_metric(self, k_folds=example[2], metric=example[3])
            test_pred.i_check_create_kfold_datasets(self, example[2])
            test_pred.i_check_create_kfold_models(self, example[2])
            test_pred.i_check_create_all_kfold_cross_validations(self, example[2])
            test_pred.i_check_feature_selection(self, example[4], example[3], example[5])

    def test_scenario3(self):
        """
            Scenario: Successfully building feature selection from dataset setting objective:
                Given I create BigML dataset uploading train "<data>" file in "<output>"
                And I check that the source has been created
                And I check that the dataset has been created
                And I create BigML feature selection <kfold>-fold cross-validations for "<objective>" improving "<metric>"
                And I check that the <kfold>-datasets have been created
                And I check that the <kfold>-models have been created
                And I check that all the <kfold>-fold cross-validations have been created
                Then the best feature selection is "<selection>", with "<metric>" of <metric_value>

                Examples:
                | data                | objective     |output                    | kfold | metric   | selection            | metric_value |
                | ../data/iris_2f.csv | 0             |./scenario_a_5/evaluation | 2     | r_squared| species              | 0.352845     |
                | ../data/iris_2f.csv | 0             |./scenario_a_8/evaluation | 2     | mean_squared_error| species     | 0.475200     |
        """
        print self.test_scenario3.__doc__
        examples = [
            ['data/iris_2f.csv', '0', 'scenario_a_5/evaluation', '2', 'r_squared', 'species', '0.352845'],
            ['data/iris_2f.csv', '0', 'scenario_a_8/evaluation', '2', 'mean_squared_error', 'species', '0.475200']]
        for example in examples:
            print "\nTesting with:\n", example
            test_pred.i_create_dataset(self, data=example[0], output=example[2])
            test_pred.i_check_create_source(self)
            test_pred.i_check_create_dataset(self)
            test_pred.i_create_kfold_cross_validation_objective(self, k_folds=example[3], objective=example[1], metric=example[4])
            test_pred.i_check_create_kfold_datasets(self, example[3])
            test_pred.i_check_create_kfold_models(self, example[3])
            test_pred.i_check_create_all_kfold_cross_validations(self, example[3])
            test_pred.i_check_feature_selection(self, example[5], example[4], example[6])

    def test_scenario4(self):
        """
            Scenario: Successfully building feature selection from filtered dataset setting objective:
                Given I create BigML dataset uploading train "<data>" file in "<output>"
                And I check that the source has been created
                And I check that the dataset has been created
                And I filter out field "<field>" from dataset and log to "<output_dir>"
                And I check that the new dataset has been created
                And I create BigML feature selection <kfold>-fold cross-validations for "<objective>" improving "<metric>"
                And I check that the <kfold>-datasets have been created
                And I check that the <kfold>-models have been created
                And I check that all the <kfold>-fold cross-validations have been created
                Then the best feature selection is "<selection>", with "<metric>" of <metric_value>

                Examples:
                | data                 | field               | objective     |output                    | output_dir | kfold | metric   | selection   | metric_value |
                | ../data/iris_2fd.csv | sepal length        | species         |./scenario_a_6/evaluation |./scenario_a_6 | 2     | recall   | petal width | 100.00%     |
        """
        print self.test_scenario4.__doc__
        examples = [
            ['data/iris_2fd.csv', 'sepal length', 'species', 'scenario_a_6/evaluation', 'scenario_a_6', '2', 'recall', 'petal width', '100.00%']]
        for example in examples:
            print "\nTesting with:\n", example
            test_pred.i_create_dataset(self, data=example[0], output=example[3])
            test_pred.i_check_create_source(self)
            test_pred.i_check_create_dataset(self)
            dataset.i_filter_field_from_dataset(self, field=example[1], output_dir=example[4])
            test_pred.i_check_create_new_dataset(self)
            test_pred.i_create_kfold_cross_validation_objective(self, k_folds=example[5], objective=example[2], metric=example[6])
            test_pred.i_check_create_kfold_datasets(self, example[5])
            test_pred.i_check_create_kfold_models(self, example[5])
            test_pred.i_check_create_all_kfold_cross_validations(self, example[5])
            test_pred.i_check_feature_selection(self, example[7], example[6], example[8])

    def test_scenario5(self):
        """
            Scenario: Successfully building nodes threshold analysis from dataset:
                Given I create BigML dataset uploading train "<data>" file in "<output>"
                And I check that the source has been created
                And I check that the dataset has been created
                And I create BigML nodes analysis from <min_nodes> to <max_nodes> by <nodes_step> with <kfold>-cross-validation improving "<metric>"
                And I check that the <kfold>-datasets have been created
                And I check that the <kfold>-models have been created
                And I check that all the <kfold>-fold cross-validations have been created
                Then the best node threshold is "<node_threshold>", with "<metric>" of <metric_value>

                Examples:
                | data                | output                  | min_nodes | max_nodes | nodes_step | kfold | metric   | node_threshold   | metric_value |
                | ../data/iris.csv | ./scenario_a_4/evaluation | 3         | 14        | 2         |2     | precision  | 9                | 94.71%         |
        """
        print self.test_scenario5.__doc__
        examples = [
            ['data/iris.csv', 'scenario_a_4/evaluation', '3', '14', '2', '2', 'precision', '9', '94.71%']]
        for example in examples:
            print "\nTesting with:\n", example
            test_pred.i_create_dataset(self, data=example[0], output=example[1])
            test_pred.i_check_create_source(self)
            test_pred.i_check_create_dataset(self)
            test_pred.i_create_nodes_analysis(self, min_nodes=example[2], max_nodes=example[3], nodes_step=example[4], k_fold=example[5], metric=example[6])
            test_pred.i_check_create_kfold_datasets(self, example[5])
            test_pred.i_check_create_kfold_models(self, example[5])
            test_pred.i_check_create_all_kfold_cross_validations(self, example[5])
            test_pred.i_check_node_threshold(self, example[7], example[6], example[8])

    def test_scenario6(self):
        """
            Scenario: Successfully building feature selection from dataset excluding features:
                Given I create BigML dataset uploading train "<data>" file in "<output>"
                And I check that the source has been created
                And I check that the dataset has been created
                And I create BigML feature selection <kfold>-fold cross-validations excluding "<features>" with separator "<args_separator>" improving "<metric>"
                And I check that the <kfold>-datasets have been created
                And I check that the <kfold>-models have been created
                And I check that all the <kfold>-fold cross-validations have been created
                Then the best feature selection is "<selection>", with "<metric>" of <metric_value>

                Examples:
                | data                | output                    | kfold | features              | args_separator | metric   | selection   | metric_value |
                | ../data/iris.csv | ./scenario_a_7/evaluation | 2     | petal length!sepal width | !              | accuracy | petal width | 95.33%      |
        """
        print self.test_scenario6.__doc__
        examples = [
            ['data/iris.csv', 'scenario_a_7/evaluation', '2', 'petal length!sepal width', '!', 'accuracy', 'petal width', '95.33%']]
        for example in examples:
            print "\nTesting with:\n", example
            test_pred.i_create_dataset(self, data=example[0], output=example[1])
            test_pred.i_check_create_source(self)
            test_pred.i_check_create_dataset(self)
            test_pred.i_create_kfold_cross_validation_separator_metric_no_fields(self, k_folds=example[2], features=example[3], args_separator=example[4], metric=example[5])
            test_pred.i_check_create_kfold_datasets(self, example[2])
            test_pred.i_check_create_kfold_models(self, example[2])
            test_pred.i_check_create_all_kfold_cross_validations(self, example[2])
            test_pred.i_check_feature_selection(self, example[6], example[5], example[7])

    def test_scenario7(self):
        """
            Scenario: Successfully building feature selection for a category from dataset:
                Given I create BigML dataset uploading train "<data>" file with attributes "<attributes>" in "<output>"
                And I check that the source has been created
                And I check that the dataset has been created
                And I create BigML feature selection <kfold>-fold cross-validations improving "<metric>" for category "<category>"
                And I check that the <kfold>-datasets have been created
                And I check that the <kfold>-models have been created
                And I check that all the <kfold>-fold cross-validations have been created
                Then the best feature selection is "<selection>", with "<metric>" of <metric_value>

                Examples:
                | data                | attributes | output                    | kfold | metric   | category | selection   | metric_value
                | ../data/spam.csv    | ../data/spam_attributes.json |./scenario_a_9/evaluation | 2     | recall   | spam     | Message     | 61.24%
        """
        print self.test_scenario7.__doc__
        examples = [
            ['data/spam.csv', 'data/spam_attributes.json', 'scenario_a_9/evaluation', '2', 'recall', 'spam', 'Message', '61.24%']]
        for example in examples:
            print "\nTesting with:\n", example
            test_pred.i_create_dataset_with_attributes(self, data=example[0], attributes=example[1], output=example[2])
            test_pred.i_check_create_source(self)
            test_pred.i_check_create_dataset(self)
            test_pred.i_create_kfold_cross_validation_metric_category(self, k_folds=example[3], metric=example[4], category=example[5])
            test_pred.i_check_create_kfold_datasets(self, example[3])
            test_pred.i_check_create_kfold_models(self, example[3])
            test_pred.i_check_create_all_kfold_cross_validations(self, example[3])
            test_pred.i_check_feature_selection(self, example[6], example[4], example[7])
