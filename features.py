#Ploting the topmost important features
def plot_top_features(pipeline):
    feature_importances = pipeline.named_steps['model'].feature_importances_
    feature_names = np.array(pipeline.named_steps['preprocessor'].transformers_[0][2].tolist() +
                             pipeline.named_steps['preprocessor'].transformers_[1][1].get_feature_names_out().tolist())
    importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importances})
    importance_df = importance_df.sort_values(by='Importance', ascending=False)

#Feature importance
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Importance', y='Feature', data=importance_df.head(10))
    plt.title('Top 10 Important Features')
    plt.xlabel('Importance')
    plt.ylabel('Feature')
    plt.show()
