class TestIrisPrediction:
    def test_get_error(self, client, data_dict):
        rv = client.get('/iris/', json=data_dict)
        assert rv.status_code == 405

    def test_put_error(self, client, data_dict):
        rv = client.put('/iris/', json=data_dict)
        assert rv.status_code == 405

    def test_patch_error(self, client, data_dict):
        rv = client.patch('/iris/', json=data_dict)
        assert rv.status_code == 405

    def test_post_prediction(self, client, data_dict):
        rv = client.post('/iris/', json=data_dict)
        assert rv.status_code == 200

        json_reponse = rv.json
        assert json_reponse.get('prediction')
        prediction = json_reponse['prediction']

        assert len(prediction) == 3
        assert all([p >= 0 and p <= 1 for p in prediction])

    def test_post_prediction_validation_error(self, client, data_dict):
        for field in data_dict.keys():
            temp_data_dict = dict(data_dict)
            del temp_data_dict[field]
            rv = client.post('/iris/', json=temp_data_dict)
            assert rv.status_code == 400

            json_reponse = rv.json
            assert json_reponse['errors'][field]

