<link rel="stylesheet" type='text/css' href='main.css' />

<div class='wrapper'>

    <div class='logo'>
        <img src='logo.png'></img>
    </div>

    <div class='form'>
        <form method='POST' action='/query'>
            <input class='input-field' name="value" type="text" />
            <input class='submit-button' type="submit" />
        </form>
    </div>

    %if values:
        <div class='output'>
            <table class='table'>
                <caption>Your output</caption>
                <thead>
                    <th></th>
                    <th>Field</th>
                    <th>Value</th>
                </thead>
                <tbody>
                    %for value in values:
                        <tr class='row'>
                            <td>
                                {{value}}
                            </td>
                            <td>
                                {{values[value]}}
                            </td>
                        </tr>
                    %end
            </table>
        </div>
    %end
</div>


